import numpy as np
hbar = 1.055e-34 #eV s
alpha = 1/137
c = 299792458 #m/s
# m_e = 510.998e3 #eV
# eV_to_J = 1.60217663*10**(-19)


a_0 = 5.29 * 10**(-11) #m
a_s = 10 * a_0 #scattering length
w_ho = 2*np.pi * 472 #1/s #harmonic oscillator potential
# m_K = 39*931.5e9 #eV #39K
m_K = 6.4761e-26 #kg #39K

a_ho = np.sqrt(hbar/w_ho/m_K)
R_TF = lambda N: a_ho * (15*N*a_s/a_ho)**(1/5)
mu = lambda N: 1/2 * m_K * w_ho**2 * R_TF(N)**2
g = 4*np.pi*hbar**2 * a_s/m_K
n = lambda N: mu(N)/g
# n = lambda N: N/R_TF(N)**3
v = lambda N: 2*hbar/m_K * np.sqrt(np.pi * a_s * n(N)) #Speed of sound
L_h = lambda N: 1/np.sqrt(8*np.pi*n(N)*a_s) #healing length
gamma = lambda N: n(N) * a_s**3
frac_TF = lambda N: N * a_s / a_ho
print(f"Problem 1)")
N = 10000
print(f"{N = }")
print(f"\tR_TF = {R_TF(N):.4e} m")
print(f"\tv = {v(N):.4e} m/s")
print(f"\tL_h = {L_h(N):.4e} m")
print(f"\tgamma = {gamma(N):.4e}")
print(f"TF param = {frac_TF(N):.3f}")

N = 100000
print(f"{N = }")
print(f"\tR_TF = {R_TF(N):.4e} m")
print(f"\tv = {v(N):.4e} m/s")
print(f"\tL_h = {L_h(N):.4e} m")
print(f"\tgamma = {gamma(N):.4e}")
print(f"TF param = {frac_TF(N):.3f}")

N = 1000000
print(f"{N = }")
print(f"\tR_TF = {R_TF(N):.4e} m")
print(f"\tv = {v(N):.4e} m/s")
print(f"\tL_h = {L_h(N):.4e} m")
print(f"\tgamma = {gamma(N):.4e}")
print(f"TF param = {frac_TF(N):.3f}")