let is_pow2 x = (x land (x - 1)) == 0


(*TODO: Optimize *)
let rec get_nearest_pow2 = function
  | x when (is_pow2 x) -> x
  | x -> get_nearest_pow2 (x + 1)


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


let mat_mul_strassen m1 m2 =

  let get_squares m dim =
    let square = mat_sub_square m in
    (square 0 0 dim,
     square dim 0 dim,
     square 0 dim dim,
     square dim dim dim) in

  let rec sqr_mul dim m1 m2  =
    match dim with
    | 0 -> Array.make_matrix 0 0 0
    | 1 -> Array.make_matrix 1 1 ( (m1.(0).(0)) * (m2.(0).(0)) )
    | _ -> let minor_mult = sqr_mul (dim / 2) in 
           let m1_lu, m1_ld, m1_ru, m1_rd = get_squares m1 (dim / 2) in
           let m2_lu, m2_ld, m2_ru, m2_rd = get_squares m2 (dim / 2) in
           let p1 = minor_mult m1_lu (mat_op ( - ) m2_ru m2_rd) in
           let p2 = minor_mult (mat_op ( + ) m1_lu m1_ru) m2_rd in
           let p3 = minor_mult (mat_op ( + ) m1_ld m1_rd) m2_lu in
           let p4 = minor_mult m1_rd (mat_op ( - ) m2_ld m2_lu) in
           let p5 = minor_mult
             (mat_op ( + ) m1_lu m1_rd)
             (mat_op ( + ) m2_lu m2_rd) in
           let p6 = minor_mult
             (mat_op ( - ) m1_ru m1_rd)
             (mat_op ( + ) m2_ld m2_rd) in
           let p7 = minor_mult
             (mat_op ( - ) m1_lu m1_ld)
             (mat_op ( + ) m2_lu m2_ru) in
           let q1 = mat_op ( + )
             (mat_op ( - ) (mat_op ( + ) p5 p4) p2) p6 in
           let q2 = mat_op ( + ) p1 p2 in
           let q3 = mat_op ( + ) p3 p4 in
           let q4 = mat_op ( - )
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
      (padded_dim - m1_height), (padded_dim - m1_width) in
    let m2_height_diff, m2_width_diff =
      (padded_dim - m2_height), (padded_dim - m2_width) in
    Some (mat_sub
           (sqr_mul
             (padded_dim)
             (mat_pad m1 m1_height_diff m1_width_diff)
             (mat_pad m2 m2_height_diff m2_width_diff))
           0 0 m1_height m2_width)
