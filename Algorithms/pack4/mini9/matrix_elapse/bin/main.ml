let read_lines file =
  let contents = In_channel.with_open_bin file In_channel.input_all in
  String.split_on_char '\n' contents

let write_lines lines file  =
  let channel = Out_channel.open_text file in
  List.fold_left (fun () line -> (Out_channel.output_string channel (line ^ "\n"))) () lines

let profile (thunk: unit -> unit) : Core.Time_ns.Span.t =
  let now_ref = ref Core.Time_ns.min_value_representable and
      end_ref = ref Core.Time_ns.max_value_representable in
  now_ref := Core.Time_ns.now ();
  thunk ();
  end_ref := Core.Time_ns.now ();
  Core.Time_ns.abs_diff (!end_ref) (!now_ref)

let test_algorithms (thunks: (unit -> unit) list) results_filename = 
  let results = List.map (fun th -> (Core.Time_ns.Span.to_ns (profile th))) thunks in
  write_lines (List.map string_of_float results) results_filename

let input_matrix filename =
  let lines = read_lines filename in
  lines 
  |> (List.map (fun nxt -> (String.split_on_char ' ' nxt))) 
  |> (List.map (List.map int_of_string)) 
  |> (List.map (Array.of_list)) 
  |> Array.of_list 

let is_pow2 x = (x land (x - 1)) == 0
  
let get_nearest_pow2 = function
  | x when (is_pow2 x) -> x
  | x ->
    let int_size = Sys.int_size in
    let rec do_or (n: int) (d: int) =
      if d >= int_size 
      then n 
      else do_or (n lor (n lsr d)) (d * 2) in
    (do_or (x - 1) 1) + 1

let mat_height m =
  Array.length m


let mat_width m =
  Array.length (m.(0))


let mat_dims m =
  ((mat_height m), (mat_width m))


let mat_sub m row_pos column_pos height width =
  Array.map
    (fun a -> (Array.sub a column_pos width))
    (Array.sub m row_pos height)


let mat_sub_square m row_pos column_pos dim =
  mat_sub m row_pos column_pos dim dim


let mat_op f m1 m2 =
  Array.map2 (Array.map2 f) m1 m2

let mat_concat_horizontal m1 m2 =
  Array.map2 (Array.append) m1 m2


let mat_pad m rows_num columns_num =
  let height, width = mat_dims m in
  Array.append
    (mat_concat_horizontal m (Array.make_matrix height columns_num 0))
    (Array.make_matrix rows_num (width + columns_num) 0)


let mat_get_row m row =
  Array.to_list m.(row)


let mat_get_column m column =
  let rec get_from_kth_rev col_list k =
    if k <= 0
    then col_list
    else get_from_kth_rev ((m.(k).(column)) :: col_list) (k - 1) in
  get_from_kth_rev [] (mat_height m)


let dot_product (v1: int list) (v2: int list) =
  List.fold_left2 (fun acc a b -> acc + a * b) 0 v1 v2

(*
let mat_mul_classic m1 m2 =
  let m1_width = mat_width m1 and
      m2_height = mat_height m2 in

  if m1_width != m2_height 
  then None 
  else
    let m1_height = mat_height m1 and
        m2_width = mat_width m2 in
    let get_row row_ind =
      let mat_row = mat_get_row m1 row_ind in
      Array.init m2_width (fun i -> (dot_product mat_row (mat_get_column m2 i))) in

    Some (Array.init m1_height get_row)
  
*)
let mat_mul_strassen m1 m2 =

  let get_squares m dim =
    let square = mat_sub_square m in (
      square 0 0 dim,
      square dim 0 dim,
      square 0 dim dim,
      square dim dim dim
    ) 
  in

  let rec sqr_mul dim m1 m2  =
    match dim with
    | 0 -> Array.make_matrix 0 0 0
    | 1 -> Array.make_matrix 1 1 ( (m1.(0).(0)) * (m2.(0).(0)) )
    | _ -> 
      let minor_mult = sqr_mul (dim / 2) in
      let m1_lu, m1_ld, m1_ru, m1_rd = get_squares m1 (dim / 2) and
          m2_lu, m2_ld, m2_ru, m2_rd = get_squares m2 (dim / 2) in
      let p1 = minor_mult m1_lu (mat_op ( - ) m2_ru m2_rd) and
          p2 = minor_mult (mat_op ( + ) m1_lu m1_ru) m2_rd and
          p3 = minor_mult (mat_op ( + ) m1_ld m1_rd) m2_lu and
          p4 = minor_mult m1_rd (mat_op ( - ) m2_ld m2_lu) and
          p5 = minor_mult
            (mat_op ( + ) m1_lu m1_rd)
            (mat_op ( + ) m2_lu m2_rd) and
          p6 = minor_mult
            (mat_op ( - ) m1_ru m1_rd)
            (mat_op ( + ) m2_ld m2_rd) and
          p7 = minor_mult
            (mat_op ( - ) m1_lu m1_ld)
            (mat_op ( + ) m2_lu m2_ru) in
          let q1 = mat_op ( + )
            (mat_op ( - ) (mat_op ( + ) p5 p4) p2) p6 and
          q2 = mat_op ( + ) p1 p2 and
          q3 = mat_op ( + ) p3 p4 and
          q4 = mat_op ( - )
            (mat_op ( - ) (mat_op ( + ) p1 p5) p3) p7 in
      Array.append
        (mat_concat_horizontal q1 q2)
        (mat_concat_horizontal q3 q4) in

  match ((mat_dims m1), (mat_dims m2)) with
  | ((_, m1_width), (m2_height, _)) when (m1_width != m2_height) -> None
  | ((m1_height, m1_width), (m2_height, m2_width)) ->
    let padded_dim =
      get_nearest_pow2
        (List.fold_right max
          ([m1_height; m1_width; m2_width]) 0) in
    let m1_height_diff, m1_width_diff =
          (padded_dim - m1_height), (padded_dim - m1_width) and
        m2_height_diff, m2_width_diff =
          (padded_dim - m2_height), (padded_dim - m2_width) in
    Some (
      mat_sub
        (sqr_mul
          (padded_dim)
          (mat_pad m1 m1_height_diff m1_width_diff)
          (mat_pad m2 m2_height_diff m2_width_diff))
          0 0 m1_height m2_width
    )


let () = 
  let thunks = ref [] in
  for i = 0 to 19 do
    let matrix1 = input_matrix ("first_matrix_" ^ (string_of_int i)) in
    let matrix2 = input_matrix ("second_matrix_" ^ (string_of_int i)) in
    thunks := (fun () -> (ignore (mat_mul_strassen matrix1 matrix2))) :: (!thunks)
  done;

  test_algorithms !thunks "results"
 