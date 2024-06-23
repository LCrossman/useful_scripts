#!/usr/bin/R


require("rhierbaps")
require("cultevo")

args = commandArgs(trailingOnly=TRUE)

if (length(args)<1) {
   stop("At least one filenames must be supplied)", call.=FALSE)
} else if (length(args)==1) {
   seqfile = args[1]
  }



load_fasta <- function(alignment_file){

   library(ape) 
   seqs <- read.FASTA(alignment_file, type="AA")
   seq_names <- labels(seqs)
   seqs <- as.character(as.matrix(seqs))
   rownames(seqs) <- seq_names

   seqs[is.na(seqs)] <- "-"
   conserved <- colSums(t(t(seqs)==seqs[1,]))==nrow(seqs)

   seqs <- seqs[, !conserved]

   is_singleton <- apply(seqs,2,function(x){
       tab <- table(x)
       return(x %in% names(tab)[tab==1])
       })

   seqs[is_singleton] <- "-"
   seqs[seqs=="X"] <- "-"

   snp_mat <- seqs
   return(snp_mat)

}

hamming_distance <- function(vec1, vec2) {
  sum(vec1 != vec2)
}

calculate_hamming_distances <- function(df) {
  num_rows <- nrow(df)
  hamming_distances <- matrix(0, nrow = num_rows, ncol = num_rows)
  
  for (i in 1:num_rows) {
    for (j in 1:num_rows) {
      hamming_distances[i, j] <- hamming_distance(df[i,], df[j,])
    }
  }
  
  rownames(hamming_distances) <- rownames(df)
  colnames(hamming_distances) <- rownames(df)
  
  return(hamming_distances)
}

fasta.file.name <- seqfile
snp.matrix <- load_fasta(fasta.file.name)
hamming <- calculate_hamming_distances(as.data.frame(snp.matrix))
write.table(hamming, "hammingdistances.xls", quote=FALSE, sep="\t", row.names=TRUE, col.names=TRUE)
min(hamming)
max(hamming)
