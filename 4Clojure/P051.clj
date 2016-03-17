;; Advanced Destructuring
;; Here is an example of some more sophisticated destructuring.

(= [1 2 [3 4 5] [1 2 3 4 5]] (let [[a b & c :as d] (list 1 2 3 4 5)]
                               [a b c d]))
