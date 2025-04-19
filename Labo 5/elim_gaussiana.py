#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Eliminacion Gausianna
"""
import numpy as np

def elim_gaussiana(A):
    cant_op = 0
    m=A.shape[0]            # Cant rows
    n=A.shape[1]            # Cant cols
    Ac = A.copy()
    
    if m!=n:
        print('Matriz no cuadrada')
        return
    
    ## desde aqui -- CODIGO A COMPLETAR
    for i in range(0,n):
        for j in range(i + 1, m):
            if Ac[j][i] != 0:
                # multi es la ctte que multiplico a la fila que estoy restando a mi fila actual
                multi = Ac[j][i] / Ac[i][i]
                # Pongo toda la fila como corresponde
                for k in range(i+1,n):
                    Ac[j][k] = Ac[j][k] - (multi * Ac[i][k])
                    cant_op += 2
                cant_op += 1

                # Pongo el valor de lo que iria en L en la posicion actual
                Ac[j][i] = multi

#    for k in range(0, m):
#        for i in range(k+1, m):
#            for j in range(i, n):
#                Ac[i][j] = Ac[i][j] - Ac[i][k]/Ac[k][k] * Ac[i - 1][j]
#                cant_op += 3


    ## hasta aqui
            
    L = np.tril(Ac,-1) + np.eye(A.shape[0]) 
    U = np.triu(Ac)
    
    return L, U, cant_op


def main():
    n = 7
    B = np.eye(n) - np.tril(np.ones((n,n)),-1) 
    B[:n,n-1] = 1
    print('Matriz B \n', B)
    
    L,U,cant_oper = elim_gaussiana(B)
    
    print('Matriz L \n', L)
    print('Matriz U \n', U)
    print('Cantidad de operaciones: ', cant_oper)
    print('B=LU? ' , 'Si!' if np.allclose(np.linalg.norm(B - L@U, 1), 0) else 'No!')
    print('Norma infinito de U: ', np.max(np.sum(np.abs(U), axis=1)) )

if __name__ == "__main__":
    main()
    
    