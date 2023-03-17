let is_pow2 x = (x land (x - 1)) == 0

let list_vec_dot xs ys =
  List.fold_left ( + ) 0 (List.map2 ( * ) xs ys)

let list_of n x =
  let rec make_list xs k =
    match k with
    | 0 -> xs
    | _ -> make_list (x :: xs) (k - 1) in
  make_list [] n


(*TODO: Optimize *)
let rec get_nearest_pow2 = function
  | x when (is_pow2 x) -> x
  | x -> get_nearest_pow2 (x + 1)


type matrix = {
  flat_array: int array;
  height: int;
  width: int;
  padded_dim: int;
}


let matrix_make height width num =
  let padded_dim = max (get_nearest_pow2 width) (get_nearest_pow2 height) in
  {
    flat_array =
      Array.append
        (Array.concat
          (list_of height (Array.append (Array.make width num)
          (Array.make (padded_dim - width) 0))))
        (Array.concat
          (list_of (padded_dim - height) (Array.make padded_dim 0)));
    height = height;
    width = width;
    padded_dim = padded_dim
  }


let matrix_get_column n mat =
  let rec get_from_kth_row k column =
    match k with
    | k when (k >= mat.height) -> List.rev column
    | k -> 
      get_from_kth_row
        (k + 1) 
        ((mat.flat_array.(n + (k * mat.padded_dim))) :: column) in
  (get_from_kth_row 0 [])

let matrix_get_row n mat =
  (Array.to_list
    (Array.sub
      mat.flat_array 
      (n * mat.padded_dim) 
      mat.width))


let matrix_set row column elem mat =
  mat.flat_array.(column + (row * mat.padded_dim)) <- elem

  
let matrix_mul_classic mat1 mat2 =
  match (mat1.width, mat2.height) with
  | _ when (mat1.width != mat2.height) -> None
  | _ -> let ret_matrix = matrix_make mat2.height mat1.width 0 in 
         for row = 0 to mat1.height do
          for column = 0 to mat2.width do
            matrix_set
              row column
              (list_vec_dot (matrix_get_row row mat1) (matrix_get_column column mat2))
              ret_matrix; 
          done;
         done;
         Some ret_matrix



