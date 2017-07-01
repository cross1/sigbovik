#lang racket
;;;;;;;;;;;;;;;;;;;;;;;;
;;; sort for sig
;;;;;;;;;;;;;;;;;;;;;;;;

(define (sorted L)
  (if (equal? (sort L) (L) )
      L (sort
         L)))