import db_helpers as db
import api_helpers as api
import matplotlib.pyplot as plt
import numpy as np

rand_keywords = ["adiabatic quantum comput*", "amplitude amplification", "analog quantum simulation*", "blind quantum comput*", "boson sampling", "bqp", "bqp-complete", "charge qubit*", "circuit quantum electrodynamics", "cluster state*", "d-wave", "delegated quantum comput*", "deutsch-jozsa algorithm*", "distributed quantum comput*", "duality quantum comput*", "durr-hoyer algorithm*", "fault-tolerant quantum comput*", "flux qubit*", "geometric quantum comput*", "grover algorithm*", "grover's algorithm*", "grover's quantum search algorithm*", "hadamard gate*", "hhl algorithm*", "holonomic quantum comput*", "linear optical quantum comput*", "logical qubit*", "measurement-based quantum comput*", "nisq", "nmr quantum comput*", "noisy intermediate scale quantum", "one-way quantum comput*", "optical comput*", "qaoa", "quantum advantage", "quantum algorithm*", "quantum annealing", "quantum approximate optimization algorithm*", "quantum automata", "quantum cellular automata", "quantum circuit*", "quantum compilation", "quantum compiler*", "quantum complexity", "quantum complexity theory", "quantum comput*", "quantum computation and information", "quantum computation architectures and implementation*", "quantum computational complexity", "quantum computational logic*", "quantum computer simulation*", "quantum computing simulation*", "quantum cost*", "quantum counting algorithm*", "quantum decryption", "quantum error correction", "quantum evolutionary algorithm*", "quantum finite automata", "quantum fourier transform*", "quantum game*", "quantum gate*", "quantum genetic algorithm*", "quantum image proces*", "quantum information proces*", "quantum knot*", "quantum lattice gas automata", "quantum logic gate*", "quantum logic synthesis", "quantum logic*", "quantum machine learning", "quantum neural network*", "quantum neuron*", "quantum optimization", "quantum parallelism", "quantum phase estimation algorithm*", "quantum private comparison", "quantum programming", "quantum programming languages", "quantum query algorithm*", "quantum query complexity", "quantum recommendation", "quantum register*", "quantum search algorithm*", "quantum search*", "quantum simulation*", "quantum software", "quantum speedup", "quantum supremacy", "quantum turing machine*", "quantum verification", "quantum volume*", "quantum walk*", "shor's algorithm", "superconducting quantum comput*", "superconducting qubit*", "surface code", "topological quantum comput*", "topological qubit*", "universal quantum comput*", "variational quantum eigensolver", "variational quantum unsampling", "vqe", "bell inequalities", "bell inequality", "bell state*", "bell state measurement", "bell states", "controlled quantum communication*", "entanglement concentration*", "entanglement distillation*", "entanglement distribution", "entanglement swap*", "epr pair*", "free-space quantum communication*", "heralded single photon source*", "heralded single-photon source*", "long-distance quantum communication*", "qber", "quantum bit commitment", "quantum bit error rate*", "quantum channel*", "quantum communication*", "quantum communication channel*", "quantum communication complexity", "quantum communication network*", "quantum communications", "quantum dense coding*", "quantum dialogue", "quantum direct communication*", "quantum discord", "quantum internet", "quantum key distribution*", "quantum network*", "quantum networks", "quantum private quer*", "quantum repeater*", "quantum repeaters", "quantum router*", "quantum sealed-bid auction*", "quantum shannon theor*", "quantum state sharing", "quantum teleportation", "remote state preparation*", "superdense coding*", "the bell state measurement*", "quantum cryptogr*", "semi-quantum cryptogr*", "quantum secret sharing", "controlled quantum secure direct communication*", "quantum secure direct communication*", "deterministic secret quantum communication*", "deterministic secure quantum communication*", "quantum signature*", "quantum blind signature*", "quantum private comparison*", "quantum encryp*", "quantum authentication", "quantum identity authentication*", "secure quantum communication*", "arbitrated quantum signature*", "quantum secure communication*", "qsdc", "quantum communication security", "y-00 protocol*", "quantum steganogra*", "continuous variable quantum key distribution*", "continuous-variable quantum key distribution*", "quantum key distribution*", "measurement-device-independent quantum key distribution*", "qkd", "qkd network*", "b92", "b92 protocol*", "bb84", "bb84 protocol*", "decoy state*", "quantum key agreement", "measurement device independent", "measurement-device-independent", "semi-quantum key distribution*", "decoy state protocol*", "decoy states*", "quantum one-time pad*", "quantum key distribution network*", "quantum key distribution protocol*", "photon number splitting attack*", "quantum sensing", "quantum sensor*", "quantum metrology", "atom interferometry", "n00n state*", "atomic sensor*", "quantum gyroscope*", "quantum accelerometer*", "quantum ins", "quantum imu", "quantum magnetometer*", "quantum rf receiver*", "cold-atom interferometer*", "cold-atom gas interferometer*", "heisenberg limit*", "standard quantum limit*", "quantum inertial sens*", "quantum gravimeter*", "quantum electrometer*", "quantum radio*", "quantum receiver*", "rydberg atom sensor*", "vapor-cell sensor*", "defect-based sensor*", "scanning quantum dot microsco*", "qubit detector*", "quantum detector*", "quantum detector tomography", "quantum tomography", "quantum state tomography", "microwave bolometer*", "microwave bolometer*", "quantum illumination", "ghost imaging", "quantum dot imaging", "quantum imaging", "quantum radar*"]

x = range(2000,2022)
topic_id = 14
keywords = db.get_keywords(topic_id)
title = db.get_topic(topic_id)[2]
token = 'Your Elsevier InstToken'
key = 'Your Elsevier API Key'

usa_rand = []
china_rand = []
usa_local = []
china_local = []

for year in x:
    print(year)
    usa_rand.append(api.fetch_papers(rand_keywords, token, key, year, 'United States'))
    china_rand.append(api.fetch_papers(rand_keywords, token, key, year, 'China'))
    usa_local.append(api.fetch_papers(keywords, token, key, year, 'United States'))
    china_local.append(api.fetch_papers(keywords, token, key, year, 'China'))

print(usa_rand)
print(usa_local)
print(china_rand)
print(china_local)
print(np.corrcoef(usa_rand, usa_local))
print(np.corrcoef(china_rand, china_local))

fig, ax1 = plt.subplots() 

ax1.set_ylabel('Papers Published')
ax1.plot(x, usa_local, color = 'blue', label='United States')
ax1.plot(x, china_local, color = 'red', label='China')
ax1.set_title(title)
ax1.legend()

ax2 = ax1.twinx()
  
ax2.set_ylabel('Papers Published (Rand Keywords)')
ax2.plot(x, usa_rand, color = 'blue', label='United States', linestyle='dashed')
ax2.plot(x, china_rand, color = 'red', label='China', linestyle='dashed')

plt.show()
