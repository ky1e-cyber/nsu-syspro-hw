type 'a uf_element =
  | SetRepr of {value: 'a; rank: int}
  | Element of {value: 'a; parrent: 'a uf_element}

type 'a union_find = {
  elements: ('a, 'a uf_element) Hashtbl.t;
  sets_count: int
}

let find_representative (uf: 'a union_find) (el: 'a) =
  let rec f (uf_elem: 'a uf_element) =
    match uf_elem with
    | SetRepr repr -> repr.value
    | Element el -> f (el.parrent) in
  f (Hashtbl.find (uf.elements) el)

  let merge_sets (uf: 'a union_find) (el1: 'a) (el2: 'a) =
    let repr1 = find_representative uf el1 and
        repr2 = find_representative uf el2 in
    