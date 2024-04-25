import pandas as pd


item1=[0,0, #DEFINIMOS UN VECTOR PARA LOS VALORES RETENIDOS EN CADA TAMIZ
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO",
    "CONCRETO"]
item2= pd.Series([# creamos el vector de la malla
    "1 1/2",
    "1",
    "3/4",
    "3/8",
    "No. 4",
    "No. 10",
    "No. 20",
    "No. 40",
    "No. 60",
    "No. 100",
    "No. 200",
    "Fondo"
  ])
valor1= pd.Series([# creamos el vector de la apertura por malla
    37.5,
    25,
    19,
    9.5,
    4.75,
    2,
    0.85,
    0.425,
    0.250,
    0.150,
    0.075,
    0
  ])

valor2= pd.Series([# creamos el vector de la apertura por malla
    37.5,
    25,
    19,
    9.5,
    4.75,
    2,
    0.85,
    0.425,
    0.250,
    0.150,
    0.075,
    0
  ])

item_1=pd.DataFrame({# creamos nuestra tabla de datos con los vectores: malla, abertura y valores retenido
    "ITEM 1":item1
  })

item_2=pd.DataFrame({# creamos nuestra tabla de datos con los vectores: malla, abertura y valores retenido
    "ITEM 2":item2
  })
valor_1=pd.DataFrame({# creamos nuestra tabla de datos con los vectores: malla, abertura y valores retenido
    "PRECIO UNITARIO 1":valor1
  })
valor_2=pd.DataFrame({# creamos nuestra tabla de datos con los vectores: malla, abertura y valores retenido
     "PRECIO UNITARIO 2":valor2
  })
