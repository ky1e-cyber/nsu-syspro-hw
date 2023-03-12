let is_power2 n = n land (n - 1)

type 'a mat_square_view = {
  matrix: ('a array) array; 
  row_pos: int; 
  column_pos: int; 
  dim: int 
}

let get_mat_square_view m row_pos column_pos dim =
  {matrix = m; row_pos = row_pos; column_pos = culumn_pos; dim = dim}

let mat_square_view_op op m1 m2 =
  assert (m1.dim == m2.dim);

let matrix_mul_strassen m1 m2 =
  let rec matrix_mul m1_view m2_view =
    assert (m1_view.dim == m2_view.dim);
    match m1_view.dim with
    | 1 -> ((m1_view.matrix.(m1_view.row_pos).(m1_view.column_pos)) *
            (m2_view.matrix.(m2_view.row_pos).(m2_view.column_pos)))
    | _ -> 
  
  (* let m1_height = Array.lenght m1 in
  let m1_width = Array.lenght m1.(0) in
  let m2_height = Array.lenght m2 in
  let m2_width = Array.lenght m2.(0) in
  *)

let print_matrix m =
  for i = 0 to ((Array.length m) - 1) do
    for j = 0 to ((Array.length m.(i)) - 1) do
      print_int m.(i).(j);
      print_string " ";
    done;
    print_endline "";
  done

let () =
  let m1 = Array.make_matrix 4 4 1 in
  let m2 = Array.make_matrix 4 4 1 in
  print_matrix (matrix_mul_strassen m1 m2)



