<<<<<<< HEAD
import os 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression  # it is sckit model using this import linear 

# i am load the data set
print(os.getcwd()) 
os.chdir("D:\\Data Sets")
dataset = pd.read_csv("VC_Startups.csv")
dataset

#now we split the data
x = dataset.iloc[:,:-1]
x

y = dataset.iloc[:,4].values
y

x = dataset.iloc[:,0].values
plt.scatter(x,y , label = 'Profit vs R&D',color = 'k',s =100)
plt.xlabel('R&D')
plt.ylabel('Profit')
plt.title("Profit vs R&D")
plt.legend()
plt.show()

#Taking admin and profit
x = dataset.iloc[:,1].values
plt.scatter(x, y, label ='',color='k',s =100)
plt.xlabel("Admin")
plt.ylabel("Profit")
plt.title("Profit vs Admin Spend")
plt.legend()
plt.show()

#Taking Marketing Spend  and profit
x = dataset.iloc[:,2].values
plt.scatter(x, y, label ='',color='k',s =100)
plt.xlabel("marketing")
plt.ylabel("Profit")
plt.title("Profit vs ,Marketing")
plt.legend()
plt.show()

#Taking State Locating and profit
x = dataset.iloc[:,3].values
plt.scatter(x, y, label ='',color='k',s =100)
plt.xlabel("State")
plt.ylabel("Profit")
plt.title("Profit vs State")
plt.legend()
plt.show()

#Do a Box plot y bcz above is texual and numerical so not visualization using scatters plot
df =  dataset.iloc[:, 3:5] 
df.boxplot(column ="Profit",by = "State")

X= dataset.iloc[: , : -2].values
X

y = dataset.iloc[:,4].values
y

arr = np.ones((50,1))
arr
X = np.append(arr=np.ones((50,1)).astype(int), values=X,axis=1)
X# (50,4) 5 rows and 4 coloumns

import statsmodels.formula.api as sm
import statsmodels.regression.linear_model as sm

X_opt = X[:, [0,1,2,3]]
X_opt = np.array(X[:, [0, 1, 2, 3]], dtype=float)

print(X_opt)


regressor_OLS =sm.OLS(endog =y,exog=X_opt).fit()
regressor_OLS

=======
import os 
import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt 
from sklearn.linear_model import LinearRegression  # it is sckit model using this import linear 

# i am load the data set
print(os.getcwd()) 
os.chdir("D:\\Data Sets")
dataset = pd.read_csv("VC_Startups.csv")
dataset

#now we split the data
x = dataset.iloc[:,:-1]
x

y = dataset.iloc[:,4].values
y

x = dataset.iloc[:,0].values
plt.scatter(x,y , label = 'Profit vs R&D',color = 'k',s =100)
plt.xlabel('R&D')
plt.ylabel('Profit')
plt.title("Profit vs R&D")
plt.legend()
plt.show()

#Taking admin and profit
x = dataset.iloc[:,1].values
plt.scatter(x, y, label ='',color='k',s =100)
plt.xlabel("Admin")
plt.ylabel("Profit")
plt.title("Profit vs Admin Spend")
plt.legend()
plt.show()

#Taking Marketing Spend  and profit
x = dataset.iloc[:,2].values
plt.scatter(x, y, label ='',color='k',s =100)
plt.xlabel("marketing")
plt.ylabel("Profit")
plt.title("Profit vs ,Marketing")
plt.legend()
plt.show()

#Taking State Locating and profit
x = dataset.iloc[:,3].values
plt.scatter(x, y, label ='',color='k',s =100)
plt.xlabel("State")
plt.ylabel("Profit")
plt.title("Profit vs State")
plt.legend()
plt.show()

#Do a Box plot y bcz above is texual and numerical so not visualization using scatters plot
df =  dataset.iloc[:, 3:5] 
df.boxplot(column ="Profit",by = "State")

X= dataset.iloc[: , : -2].values
X

y = dataset.iloc[:,4].values
y

arr = np.ones((50,1))
arr
X = np.append(arr=np.ones((50,1)).astype(int), values=X,axis=1)
X# (50,4) 5 rows and 4 coloumns

import statsmodels.formula.api as sm
import statsmodels.regression.linear_model as sm

X_opt = X[:, [0,1,2,3]]
X_opt = np.array(X[:, [0, 1, 2, 3]], dtype=float)

print(X_opt)


regressor_OLS =sm.OLS(endog =y,exog=X_opt).fit()
regressor_OLS

>>>>>>> 36caba3 (Initial commit: VC Startups Linear Regression project)
