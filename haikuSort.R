muhList <- c(1,2,4,3,0,1)

sort <- function(a) {
sorted.list <- a[order(a)]
return(sorted.list)
}

print(sort(muhList))
