module type BST =
sig
  type 'a t

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
  type 'a t =
    | Leaf
    | Node of {
        value: 'a; 
        priority: int; 
        left: 'a t; right: 'a t
      }


end

let () =
  ()

