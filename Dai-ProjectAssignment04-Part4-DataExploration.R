# import needed library
library(tidyverse)

# load the Dai-ProjectAssignment04-Cleaned.csv data set into an R data frame
powerlifting_data <- read.csv("Dai-ProjectAssignment04-Cleaned.csv", header = TRUE)
powerlifting_data

# R changed values in Sex column from "F" to "FALSE" but it is supposed to mean "Female", not "FALSE"
powerlifting_data$Sex <- gsub("FALSE", "F", powerlifting_data$Sex)
powerlifting_data

# read the details about the data set
# check type of data set
class(powerlifting_data)
# check objects and variables
str(powerlifting_data)
# get the descriptive statistics of powerlifting data set
summary(powerlifting_data)

# display a few records
# get first 12 records of the data set
head(powerlifting_data, n = 12)
# check last 12 records of the data set
tail(powerlifting_data, n = 12)


# first research question -
# do female powerlifters that have high deadlift scores also
# have high squat scores?
# this question can be answered by scatter plot to see the
# if deadlift scores and squat scores are correlated

# display appropriate and labeled summary statistics and visualizations for squat and deadlift
# check the statistics info of squat column
summary(powerlifting_data$Squat)
# check the statistics info of deadlift column
summary(powerlifting_data$Deadlift)


# check the distribution of squat and deadlift
# squat histogram
ggplot(powerlifting_data, aes(x=Squat))+
  geom_histogram(binwidth=6, fill="skyblue",color="black") +
  labs(x="Squat Score (kg)",
       y="Count",
       title="2023 USPC Female Powerlifters: Squat Scores Histogram",
       subtitle="Distribution of Squat Scores",
       caption="Source: https://www.openpowerlifting.org/rankings/uspc/women/2023/by-total") +
  theme(plot.title=element_text(hjust=0.5),
        plot.subtitle=element_text(hjust=0.5),
        plot.caption=element_text(hjust=0.5)) +
  scale_y_continuous(expand=c(0, 0), limits=c(0, 35))

# deadlift histogram
ggplot(powerlifting_data, aes(x=Deadlift))+
  geom_histogram(binwidth=6, fill="skyblue",color="black") +
  labs(x="Deadlift Score (kg)",
       y="Count",
       title="2023 USPC Female Powerlifters: Deadlift Scores Histogram",
       subtitle="Distribution of Deadlift Scores",
       caption="Source: https://www.openpowerlifting.org/rankings/uspc/women/2023/by-total") +
  theme(plot.title=element_text(hjust=0.5),
        plot.subtitle=element_text(hjust=0.5),
        plot.caption=element_text(hjust=0.5)) +
  scale_y_continuous(expand=c(0, 0), limits=c(0, 45))

# plot squat vs. deadlift scatter plot
ggplot(powerlifting_data, aes(x=Squat, y=Deadlift)) + 
  geom_point() +
  geom_smooth(method="lm", se=FALSE) +
  labs(x="Squat Score (kg)",
       y="Deadlift Score (kg)",
       title="2023 USPC Female Powerlifters: Squat vs. Deadlift Scores Scatterplot",
       subtitle="Relationship between Squat and Deadlift Scores",
       caption="Source: https://www.openpowerlifting.org/rankings/uspc/women/2023/by-total") +
  theme(plot.title=element_text(hjust=0.5),
        plot.subtitle=element_text(hjust=0.5),
        plot.caption=element_text(hjust=0.5))

# deadlift records and squat records are positively correlated.
# female powerlifters that have high squat scores also have high deadlift scores.

# let's take a look at the correlation coefficient between squat and deadlift scores
cor(powerlifting_data$Squat, powerlifting_data$Deadlift, use = "complete.obs")


# second research question -
# do female powerlifters with high body weight also have high total scores in deadlift, bench, and squat?

# display appropriate and labeled summary statistics and visualizations for weight and total
# check the statistics info of weight column
summary(powerlifting_data$Weight)
# check the statistics info of total column
summary(powerlifting_data$Total)

# weight histogram
ggplot(powerlifting_data, aes(x=Weight))+
  geom_histogram(binwidth=6, fill="skyblue",color="black") +
  labs(x="Body Weight (kg)",
       y="Count",
       title="2023 USPC Female Powerlifters: Weights Histogram",
       subtitle="Distribution of Lifter Body Weights",
       caption="Source: https://www.openpowerlifting.org/rankings/uspc/women/2023/by-total") +
  theme(plot.title=element_text(hjust=0.5),
        plot.subtitle=element_text(hjust=0.5),
        plot.caption=element_text(hjust=0.5)) +
  scale_y_continuous(expand=c(0, 0), limits=c(0, 70))

# total histogram
ggplot(powerlifting_data, aes(x=Total))+
  geom_histogram(binwidth=6, fill="skyblue",color="black") +
  labs(x="Total Weight Lifted (kg)",
       y="Count",
       title="2023 USPC Female Powerlifters: Total Scores Histogram",
       subtitle="Distribution of Total Weight Lifted (Bench Press + Squat + Deadlift)",
       caption="Source: https://www.openpowerlifting.org/rankings/uspc/women/2023/by-total") +
  theme(plot.title=element_text(hjust=0.5),
        plot.subtitle=element_text(hjust=0.5),
        plot.caption=element_text(hjust=0.5)) +
  scale_y_continuous(expand=c(0, 0), limits=c(0, 20))

# plot weight vs. total scatter plot
ggplot(powerlifting_data, aes(x=Weight, y=Total)) + 
  geom_point() +
  geom_smooth(method="lm", se=FALSE) +
  labs(x="Body Weight (kg)",
       y="Total Weight Lifted (kg)",
       title="2023 USPC Female Powerlifters: Weights vs. Total Scores Scatterplot",
       subtitle="Relationship between Body Weight and Total Weight Lifted (Bench Press + Squat + Deadlift)",
       caption="Source: https://www.openpowerlifting.org/rankings/uspc/women/2023/by-total") +
  theme(plot.title=element_text(hjust=0.5),
        plot.subtitle=element_text(hjust=0.5),
        plot.caption=element_text(hjust=0.5))
# as body weight increases, the total weight lifted increases. But the correlation is weak.

# let's take a look at the correlation coefficient between the variables
cor(powerlifting_data$Weight, powerlifting_data$Total, use = "complete.obs")

# third research question -
# what age range has the highest bench scores?

# display appropriate and labeled summary statistics and visualizations for age and bench
# check the statistics info of weight column
summary(powerlifting_data$Age)
# check the statistics info of total column
summary(powerlifting_data$Bench)
# check the max age
max(powerlifting_data$Age)
# check the min age
min(powerlifting_data$Age)
# create age range column
powerlifting_data$ageRange <- cut(powerlifting_data$Age, breaks=c(10, 20, 30, 40, 50, 60, 70, 80), 
                                        labels=c("10-19", "20-29", "30-39", "40-49", "50-59",
                                                 "60-69", "70-80"), include.lowest = TRUE)
powerlifting_data

ggplot(powerlifting_data, aes(x=ageRange, y=Bench)) + 
  geom_boxplot() +
  labs(x="Age Range",
       y="Bench Score (kg)",
       title="2023 USPC Female Powerlifters: Bench Scores in Different Age Ranges",
       subtitle="Distribution of Bench Scores in Different Age Groups",
       caption="Source: https://www.openpowerlifting.org/rankings/uspc/women/2023/by-total") +
  theme(plot.title=element_text(hjust=0.5),
        plot.subtitle=element_text(hjust=0.5),
        plot.caption=element_text(hjust=0.5))
# age range 50-59 has the highest median bench score (kg) and 
# and the box height is relatively narrow.