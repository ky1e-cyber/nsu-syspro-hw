let is_pow2 x = (x land (x - 1)) == 0

let mat_height (m: ('a array) array) =
  Array.length m

let mat_width (m: ('a array) array) =
  Array.length (m.(0))

let mat_dims (m: ('a array) array) =
  ((mat_height m), (mat_width m))

let mat_sub (m: ('a array) array) row_pos column_pos height width =
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
    (Array.make_matrix rows_num (width + column_nums) 0)


let mat_pad_square m =
  match (mat_dims m) with
  | (height, width) when (height > width) ->
      mat_pad m 0 (height - width)
  | (height, width) when (height < width) ->
      mat_pad m (width - height) 0
  | _ -> m

let matrix_mul_strassen m1 m2 =
  let get_squares m dim =
    let square = mat_sub_square m in    
    (
      square 0 0 dim,
      square dim 0 dim,
      square 0 dim dim,
      square dim dim dim
    ) in

  let rec sqr_mul m1 m2 =
    assert ((mat_dims m1) = (mat_dims m2));
    match (mat_height m1) with
    | 0 -> Array.make_matrix 0 0 0
    | 1 -> Array.make_matrix 1 1 ( (m1.(0).(0)) * (m2.(0).(0)) )
    | dims -> let m1_lu, m1_ld, m1_ru, m1_rd = get_squares m1 (dims / 2) in
              let m2_lu, m2_ld, m2_ru, m2_rd = get_squares m2 (dims / 2) in
              let p1 = sqr_mul m1_lu (mat_op ( - ) m2_ru m2_rd) in
              let p2 = sqr_mul (mat_op ( + ) m1_lu m1_ru) m2_rd in
              let p3 = sqr_mul (mat_op ( + ) m1_ld m1_rd) m2_lu in
              let p4 = sqr_mul m1_rd (mat_op ( - ) m2_ld m2_lu) in
              let p5 = sqr_mul
                        (mat_op ( + ) m1_lu m1_rd)
                        (mat_op ( + ) m2_lu m2_rd) in
              let p6 = sqr_mul
                        (mat_op ( - ) m1_ru m1_rd)
                        (mat_op ( + ) m2_ld m2_rd) in
              let p7 = sqr_mul
                        (mat_op ( - ) m1_lu m1_ld)
                        (mat_op ( + ) m2_lu m2_ru) in
              let q1 = mat_op
                        ( + ) (mat_op ( - ) (mat_op ( + ) p5 p4) p2) p6 in
              let q2 = mat_op ( + ) p1 p2 in
              let q3 = mat_op ( + ) p3 p4 in
              let q4 = mat_op
                        ( - ) (mat_op ( - ) (mat_op ( + ) p1 p5) p3) p7 in
              Array.append
                (mat_concat_horizontal q1 q2)
                (mat_concat_horizontal q3 q4) in

  match ((mat_width m1), (mat_height m2)) with
  | (m1_width, m2_height) when (m1_width != m2_height) -> None
  | (m1_width, m2_height) -> let m1_padded = mat_pad_square m1 in
                             let m2_padded = mat_pad_square m2 in
