let inc (r: int ref) : int = 
  let current = !r in 
  r := (!r + 1); current


let permute_QPR x =
  if x < 0 
    then failwith "Panic! permute_QPR accepts only integers > 0";
  let large_prime = 
    if (Sys.word_size = 64) 
      then Unsigned.UInt64.of_int 4611686018427387847 (* closest <= 2^63 *)
      else Unsigned.UInt64.of_int 4294967291 (* closest <= 2^31 *)
  and
      x_64 = Unsigned.UInt64.of_int x    
  in
  if (x_64 >= large_prime) 
    then x 
    else
      (* (x_64 * x_64) mod large_prime *) 
      Unsigned.UInt64.to_int 
        Unsigned.UInt64.Infix
          .(Unsigned.UInt64.Infix
          .(x_64 * x_64) mod large_prime) 


let create_random_unique_seq (offset_seed: int) : (unit -> int) =
  if offset_seed < 0 
    then failwith "Panic! offset_seed for create_random_unique_seq must be >= 0";
  let ind = ref 0 and
      offset = (permute_QPR offset_seed) and
      xor_offset = 0x5bf03635
  in
  let generator () =
    let i = inc ind in
    if i < 0
      then failwith "Panic! generator limit exceeded (somehow).";
    permute_QPR 
      (Unsigned.UInt32.to_int 
        (Unsigned.UInt32.of_int 
          (Int.logxor xor_offset (permute_QPR (i + offset)))))
  in
  generator

module type BST =
sig

  type 'a t

  val create_emty : unit -> 'a t

  val insert : 'a -> 'a t -> 'a t

  val remove : 'a -> 'a t -> 'a t

  val find : 'a -> 'a t -> bool

  val select : int -> 'a t -> 'a option

  val min : 'a t -> 'a option

  val max : 'a t -> 'a option

  val rank : 'a -> 'a t -> int

  val to_list : 'a t -> 'a list
end


module Treap = 
struct


  type 'v node = 
    | Leaf 
    | Node of {
        left: 'v node;
        right: 'v node;
        element: 'v;
        priority: int;    
      }

  type ('k, 'v) t = {
    root: 'v node;
    (* 
      k1 > k2 => _cmp_func(k1, k2) > 0; 
      k1 == k2 => _cmp_func(k1, k2) == 0;
      else < 0
    
    *)
    _cmp_fn: ('k -> 'k -> int);
    _key_fn: ('v -> 'k);
  }
  
  let create_empty (cmp : ('v -> 'v -> int)) 
                   (key_func: ('v -> 'k)) = {
      root = Leaf;
      _cmp_fn = cmp;
      _key_fn = key_func;
    }
  
  let of_list (cmp: ('v -> 'v -> int)) 
              (key_func: ('v -> 'k)) 
              (lst: 'a list) =
    ()

  let of_sorted_list (cmp: ('a -> 'a -> int)) (lst: 'a list) = ()
  
end


let rec print_int_list lst =
  match lst with
  | x :: tail -> print_int x; print_endline ""; print_int_list tail 
  | [] -> ()


let generator_to_list (n: int) (gen : (unit -> int)) : int list =
  let rec f k acc =
    if k < 0 then acc else f (k - 1) ((gen ()) :: acc) in
  f n []

let () = print_int_list (generator_to_list 10 (create_random_unique_seq 010010100))
