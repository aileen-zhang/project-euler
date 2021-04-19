(* totient maximum: n / phi(n) maximized as product of k smallest primes *)

let prime_multiplier maximum =
  let is_prime n =
    let rec divisible a d =
      match a, d with
      | _, 1 -> false
      | a', d' when a' mod d' = 0 -> true
      | _, _ -> divisible a (d - 1)
    in match n with
      | 0 | 1 -> false
      | n' when n' < 0 -> false
      | _ -> not (divisible n (int_of_float (sqrt (float_of_int n))))
  in let rec iter n maximum product =
    match n, product with
    | n', product' when n' * product' > maximum -> product
    | n', _ when is_prime n' -> iter (n + 1) maximum (product * n)
    | _, _ -> iter (n + 1) maximum product
  in iter 2 maximum 1

(*
  let time f x =
    let t = Sys.time() in
    let fx = f x in
    Printf.printf "Execution time: %fs\n" (Sys.time() -. t);
    fx

  time prime_multiplier 1000000

  Execution time: 0.000009s
  - : int = 510510
*)
