import numpy as np

hbar = 6.626*10**(-34) /(2*np.pi)       #J*s
n = 5*10**(8)*10**(2*3)               #m^-3
e = 1.60217663 * 10**(-19)              #C
m_Ca = 6.63594433 * 10**(-26)              #kg    mass of 40Ca
m_e = 9.1093837 * 10**(-31)               #kg
m_Fe = 9.3 * 10**(-26)                      #kg
eps_0 = 8.854 * 10**(-12)                 #F/m
k_B = 1.380649 * 10**(-23)              #m^2*kg / (s^2 * K)

calc_a = lambda n: (3 / (4 * np.pi * n))**(1/3)
calc_omega_p = lambda Q, m: np.sqrt(Q**2 * n / (eps_0 * m))
calc_rQM = lambda Q, m: np.sqrt(hbar / (8 * np.pi * calc_omega_p(Q,m) * m))
calc_E_kin_zero = lambda Q, m: 0.5 * calc_omega_p(Q,m) * hbar
calc_E_kin_temp = lambda T: k_B * T


print(f"Exercise 1.a)")
a = calc_a(n)
omega_p = calc_omega_p(e, m_Ca)
r_QM = calc_rQM(e, m_Ca)

print(f"r_QM = {r_QM:.3e} m, \t a = {a:.3e} m \n")


print(f"Exercise 1.b)")
T_crit = e**2 / (680 * np.pi * eps_0 * a * k_B)
print(f"Critical temperature = {T_crit:.3e} K\n")


print(f"Exercise 1.c)")
E_kin_zero = calc_E_kin_zero(e, m_Ca)
E_kin_temp = calc_E_kin_temp(T_crit)
print(f"Zero point energy = {E_kin_zero:.3e} J, \t Thermal kinetic energy = {E_kin_temp:.3e} J\n")


print(f"Exercise 2)")
n_e = 10**(23)*10**(2*3)                  #m^-3
a = calc_a(n_e)

omega_p = calc_omega_p(e, m_e)
r_QM = calc_rQM(e, m_e)

print(f"r_QM = {r_QM:.3e} m, \t a = {a:.3e} m \n")


print(f"Exercise 3.a)")
rho = 10**(10)* 10**(-3) * 10**(2*6)                #kg / m^3
n = rho / m_Fe
Q = 26 * e

a = calc_a(n)
omega_p = calc_omega_p(Q, m_Fe)
r_QM = calc_rQM(Q, m_Fe)

print(f"r_QM = {r_QM:.3e} m, \t a = {a:.3e} m \n")

print(f"Exercise 3.b)")
T = 10**7                               #K
E_kin_temp = calc_E_kin_temp(T)
E_kin_zero = calc_E_kin_zero(Q, m_Fe)

print(f"Zero point energy = {E_kin_zero:.3e} J, \t Thermal kinetic energy = {E_kin_temp:.3e} J\n")


print(f"Exercise 3.c)")
Gamma = Q**2 / (4*np.pi * eps_0 * a * E_kin_temp)
print(f"Gamma = {Gamma:.3e} \n")

