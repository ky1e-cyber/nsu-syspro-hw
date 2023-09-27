type 'a set_representative = {
  value : 'a;
  rank : int
}

type 'a set_element = {
  value : 'a;
  parrent : 'a
}

type 'a uf_member = 
  | SetRepr of 'a set_representative
  | Element of 'a set_element

type 'a union_find = {
  elements : ('a, 'a uf_member) Hashtbl.t;
  set_count : int
}

let rec get_member (uf : 'a union_find) (el : 'a) : 'a uf_member option =
  try 
    Some (Hashtbl.find (uf.elements) el)
   with 
    Not_found -> None

(* TODO: remake with a tailrec *)
let rec get_representative (uf : 'a union_find) (el : 'a) : 'a set_representative option = 
  let f (member : 'a uf_member) =
    match member with
    | SetRepr repr -> Some repr
    | Element el -> get_representative uf el.value in
  match (get_member uf el) with
  | None -> None
  | Some member -> f member
