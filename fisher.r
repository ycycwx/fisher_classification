setwd('C://cygwin64/home/Ycy/Python/fisher')

data <- read.table('synth.tr', T)
plot(data$xs[1 : 125], data$ys[1 : 125], pch = 10)
points(data$xs[126 : 250], data$ys[126 : 250], pch = 16)

data <- read.table('synth.te', T)
plot(data$xs[1 : 500], data$ys[1 : 500], pch = 11)
points(data$xs[501 : 1000], data$ys[501 : 1000], pch = 16)

data <- read.table('train', T)
plot(data$xs[1 : 5], data$ys[1 : 5], pch = 10, xlim = c(-5, 5), ylim = c(-5, 5))
points(data$xs[6 : 12], data$ys[6 : 12], pch = 16)

data <- read.table('test', T)
plot(data$xs[1 : 4], data$ys[1 : 4], pch = 10, xlim = c(-5, 5), ylim = c(-5, 5))
points(data$xs[5 : 8], data$ys[5 : 8], pch = 16)
