
setwd('E:/01_analisis_datos/Datos_pss/data')

#librerias
library(tidyverse)
library(readr)
library(bigrquery)
library(ggplot2)
library(DataExplorer)
library(hrbrthemes)


######
########lectura de datos
df_pnt <- read_csv("PSS_Colombia_0.csv")

df_cedulas_mg <- read_csv("ciclo1_1.csv")


df_reglas <- read_csv("ciclo_2.csv")
##################

project_id <- "co-tpd-ve-twm-dev" # put your project ID here

#general
sql_string_general <- "SELECT * FROM pss.t_general"
df_general <- query_exec(sql_string_general, project = project_id, useLegacySql = FALSE)

#cedulas lideres
sql_string_cedulas <- "SELECT * FROM pss.t_cedula"
df_cedulas<- query_exec(sql_string_cedulas, project = project_id, useLegacySql = FALSE)


#cedulas reglas
sql_string_reglas <- "SELECT * FROM pss.t_reglas"
df_reglas<- query_exec(sql_string_reglas, project = project_id, useLegacySql = FALSE)



######### Analisis

plot_bar(df_general)

df_sum_gen<- filter(df_general, tipo_encuesta == 'visitasvivir' & sector=='Residuos'  )%>%
  group_by(actividad_r,Acciones_pendientes )%>%
    summarise(
      contar=n()
    )

summary(df_general)



df_general%>%
  gro
  
  ggplot( aes(x=fecha, y=value)) +
  geom_line( color="grey") +
  geom_point(shape=21, color="black", fill="#69b3a2", size=6) +
  theme_ipsum() +
  ggtitle("Evolution of bitcoin price")





##

ggplot(df_sum_gen, aes(x="", y=contar)) +


# Basic piechart
ggplot(df_sum_gen, aes(x="", y=contar, fill=actividad_r)) +
  geom_bar(stat="identity", width=1, color="white") +
  coord_polar("y", start=0) +
  
  theme_void() # remove background, grid, numeric labels







