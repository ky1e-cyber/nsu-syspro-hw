Оценка сложности:

`n = dividend.bitLength`
`m = divisor.bitLength`

На каждой итерации внутреннего цикла (`while (dividend >= multiplier * divisor)`) мы конструируем `divisor' = multiplier * divisor` следующим образом:
Делаем битовый сдвиг влево пока `divisor'` не станет больше `dividend`;
В худшем случае мы сделаем n - m + 1 сдвигов влево (тогда `divisor'.bitLength == dividend.bitLength + 1`) и 1 сдвиг вправо чтобы "выровнять";

Делаем вычитание `dividend -= multiplier * divisor` и `dividend.bitLength` станет хотя бы на 1 меньше;
Несложно заметить, что для наихудшего сценария можно взять `dividend = 11...1` и `divisor = 10...0` с `bitLength` `n` и `m` соответственно;
Также замечаем, что в нашем случае чтобы выполнилось условие выхода из цикла `while (dividend >= divisor)` нужно лишь `dividend.bitLength == (m - 1)`, что возможно через `n - m + 1` итераций внешнего цикла;
В итоге получаем со всеми действиями:
Сумму по `i = 0..(n - m + 1) : ((n - i) - m + 4)` (+ 1 проверка в конце)
Оценим сверху как `(n - m + 4) * (n - m + 1) = O( (n - m + 1)^2 )`
Если уйти от `m` и `n`, `(n - m + 1) == log_2{dividend / divisor} + 1`
=> `O( (log_2{dividend / divisor} + 1)^2 )`
