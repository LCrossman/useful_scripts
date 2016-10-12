#!/usr/bin/R

library(ape)
args = commandArgs(trailingOnly=TRUE)

if (length(args)<2) {
   stop("At least two filenames must be supplied, tree first then mapping file with tab separated two columns of sample names and factor to colour by, (e.g. species name, isolate site)", call.=FALSE)
} else if (length(args)==2) {
   treefile = args[1]
   mapfile = args[2]
  }

merge.with.order <- function(x,y, ..., sort = T, keep_order)
{
# this function works just like merge, only that it adds the option to return the merged data.frame ordered by x (1) or by y (2)
add.id.column.to.data <- function(DATA)
{
data.frame(DATA, id... = seq_len(nrow(DATA)))
}
# add.id.column.to.data(data.frame(x = rnorm(5), x2 = rnorm(5)))
order.by.id...and.remove.it <- function(DATA)
{
# gets in a data.frame with the "id..." column.  Orders by it and returns it
if(!any(colnames(DATA)=="id...")) stop("The function order.by.id...and.remove.it only works with data.frame objects which includes the 'id...' order column")
 
ss_r <- order(DATA$id...)
ss_c <- colnames(DATA) != "id..."
DATA[ss_r, ss_c]
}
 
# tmp <- function(x) x==1; 1# why we must check what to do if it is missing or not...
# tmp()
 
if(!missing(keep_order))
{
if(keep_order == 1) return(order.by.id...and.remove.it(merge(x=add.id.column.to.data(x),y=y,..., sort = FALSE)))
if(keep_order == 2) return(order.by.id...and.remove.it(merge(x=x,y=add.id.column.to.data(y),..., sort = FALSE)))
# if you didn't get "return" by now - issue a warning.
warning("The function merge.with.order only accepts NULL/1/2 values for the keep_order variable")
} else {return(merge(x=x,y=y,..., sort = sort))}
}

snip <- read.tree(treefile)
mapping <- read.delim(mapfile, header=FALSE, sep="")
df <- data.frame(snip$tip.label)
colnames(df) <- "V2"

nam <- merge.with.order(df, mapping, by="V2", sort=FALSE, all.x=TRUE, keep_order=TRUE)
nam$V3 <- as.integer(nam$V1)
nam$V3 <- as.factor(nam$V3)
library(RColorBrewer)
color_palette_function <- colorRampPalette(colors=brewer.pal(12, "Paired"), space="Lab")
diamond_color_colors <- color_palette_function(nlevels(nam$V3))
coler <- nam$V3
pdf("Treefanoutput.pdf")
plot(as.phylo(snip), tip.color=diamond_color_colors[coler], type="fan", cex=0.5, no.margin=TRUE)
dev.off()
pdf("Treephylogramoutput.pdf")
plot(as.phylo(snip), tip.color=diamond_color_colors[coler], cex=0.5, no.margin=TRUE)
dev.off()
