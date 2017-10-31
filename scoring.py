 # para hacer los reportes de puntajes
import numpy as np

# Utility function to report best scores
def report_multi(results, nombres_scoring, n_top=10):
    for s in sorted(nombres_scoring):
        print ("Puntajes usando "+s)
        for i in range(1, n_top + 1):
            candidates = np.flatnonzero(results['rank_test_'+s] == i)
            for candidate in candidates:
                print("Puesto: {0}".format(i))
                print("Promedio training score: {0:.3f} (std: {1:.3f})".format(
                    results['mean_train_'+s][candidate],
                    results['std_train_'+s][candidate]))
                print("Promedio validation score: {0:.3f} (std: {1:.3f})".format(
                    results['mean_test_'+s][candidate],
                    results['std_test_'+s][candidate]))
                print("Hyper-parametros: {0}".format(results['params'][candidate]))
                print("")
        print("------------------------------------")
        print("------------------------------------")
        print("------------------------------------")


# Utility function to report best scores
def report_single(results, n_top=10):
    for i in range(1, n_top + 1):
        candidates = np.flatnonzero(results['rank_test_score'] == i)
        for candidate in candidates:
            print("Model with rank: {0}".format(i))
            print("Mean training score: {0:.3f} (std: {1:.3f})".format(
                results['mean_train_score'][candidate],
                results['std_train_score'][candidate]))
            print("Mean validation score: {0:.3f} (std: {1:.3f})".format(
                results['mean_test_score'][candidate],
                results['std_test_score'][candidate]))
            print("Parameters: {0}".format(results['params'][candidate]))
            print("")
