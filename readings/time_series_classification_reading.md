# Time Series Classification Readings
## references
1. [basic introduction](https://developer.ibm.com/learningpaths/get-started-time-series-classification-api/what-is-time-series-classification/)
2. [DS-GA 3001. Probabilistic Time Series Analysis](https://github.com/charlieblue17/pTSAFall2018)
### reading notes on lecture 1. 
- think of time series as a sequence of random variables $\{X_1\dots X_n\}$ where they are not iid. 
- stats to keep in mind are mean, covariance auto correlation function (ie the similarity between observations of a random variable as a function of the time lag between them.)  $\rho_{X}(t,u)=\frac{cov(X_t, X_U)}{\sqrt{cov(X_{t}X_{t})cov(X_{u}X_{u})}}$
- recall formally
    - $var(x)=E[(x-E[x])^2]$
    - $cov(x,y)=E[(x-E[x])(y-E[y])]=E[xy]-E[x]E[y]$
- let $X=\{X_1...X_n\}$ be a sequence of random variables (ie a random vector $\in \mathbb{R}^{n}$) let $a=\{a_1..a_n\}$ be a sequence of constants (ie a deterministic vector $\in \mathbb{R}^{n}$)
- we can define a new random vector as a linear a combination $U=a^{T}X=\Sigma_{i=1}^{n}a_iX_i$ 
- for two arbitrary linear combinations $U=a^{T}X=\Sigma_{i=1}^{n}a_iX_i$ , $V=b^{T}Y=\Sigma_{i=1}^{n}b_iY_i$ we can find there covariance as $cov(U,V)=E[U*V]-E[U]E[V]=E[\Sigma_{i=1}^{n}a_iX_i*\Sigma_{j=1}^{n}b_jY_j]-E[\Sigma_{i=1}^{n}a_iX_i]E[\Sigma_{j=1}^{n}b_jY_j]=\Sigma_{i}\Sigma_{j}a_ib_j(E[X_iY_J]-E[X_i]E[X_j])=\Sigma_{i}\Sigma_{j}a_ib_jcov(X_i,Y_j)=a^{t}cov(X,Y)b$
- we can define a random walk as $x_{t}=\delta+x_{t-1}+w_t$ where $w_t\sim \mathcal{N}(0,\sigma^2)$
- then we can recursively write  $x_{t}=\delta+x_{t-1}+w_t=\delta(t)+\Sigma_{i\leq t}w_i$
- and further see $E[x_t]=t\delta$, $cov(x_t,x_u)=min(t,u)\sigma^2$
- we could assume strong stationary that is for a time series X $\forall t,h,j$ we assume all subsets $\{X_t...X_{t+k}\},\{X_{t+h}...X_{t+h+k}\}$ are identically distributed
- for $k=0$ this implies all $X_i$ have the same marginal pdf
- for $k=1$ all single variables have the same pairwise dependance 
- there are a few other assumptions one could look through. None seem relevant to this work though
-