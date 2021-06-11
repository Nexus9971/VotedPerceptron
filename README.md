Il progetto si propone l'obbiettivo di implementare e testare il funzionamento del Voted-Perceptron una variante dell'algoritmo Perceptron, descritta in Freund & Schapire 1999.

INPUT: percentuale del dataset da utilizzare per il training (e quindi il test), numero di addestramenti/predizioni (ho generalizzato k=10 richiesto nel file delle istruzioni sull'esame), numero di iterazioni massime (epoche) per il Voted Perceptron, scelta Dataset da caricare (1, 2, o 3)

OUTPUT: matrice di confusione di ogni addestramento/predizione, media, varianza e deviazione standard
di accuratezza, precisione, f1 e recall e tempo necessario all'esecuzione del programma

Il codice è strutturato in tre file:

-main: codice che carica i datasets, suddivide (randomicamente e con percentuale scelta dall'utente) in train e test , chiama l'algoritmo, effettua la predizione e stampa dei dati volti a indicare l'efficienza dell'algoritmo

-utils: codice contenente un insieme di funzioni volte a semplificare alcune operazioni matematiche, di stampa dati e caricamento dataset che vengono effettuate più volte durante il ciclo di esecuzione del programma, inoltre permettono di mantenere il codice snello e pulito

-Voted_Perceptron: classe che implementa un costruttore che imposta il numero massimo di iterazioni (epoche) dell'algoritmo, un metodo fit che permette all'algoritmo di ricavare una successione di iperpiani (sui punti X,Y di addestramento) con relativi costi, metodo predict che successivamente al fit consente di classificare dei punti x (di test) presi in input (da verificare sulle y di test).

NOTE: Per il corretto funzionamento del programma è necessario inserire nella root di progetto i .csv dei Dataset citati successivamente.

RIFERIMENTI: I dataset sono stati presi dall'UCI Machine Learning Repository, quelli implementati presentano attributi afferenti la classificazione in chimica e sono:

-https://archive.ics.uci.edu/ml/datasets/QSAR+androgen+receptor "QSAR ANDROGEN RECEPTOR" (Dataset 1) F. Grisoni, V. Consonni, D. Ballabio, (2019) Machine Learning Consensus to Predict the Binding to the Androgen Receptor within the CoMPARA project, Journal of chemical information and modeling, 59, 1839-1848; doi: 10.1021/acs.jcim.8b00794

-https://archive.ics.uci.edu/ml/datasets/QSAR+oral+toxicity "QSAR ORAL TOXICITY (Dataset 2) D. Ballabio, F. Grisoni, V. Consonni, R. Todeschini (2019), Integrated QSAR models to predict acute oral systemic toxicity, Molecular Informatics, 38, 180012; doi: 10.1002/minf.201800124

-https://archive.ics.uci.edu/ml/datasets/QSAR+biodegradation "QSAR BIODEGRADATION" (Dataset 3) Mansouri, K., Ringsted, T., Ballabio, D., Todeschini, R., Consonni, V. (2013). Quantitative Structure - Activity Relationship models for ready biodegradability of chemicals. Journal of Chemical Information and Modeling, 53, 867-878