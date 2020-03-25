from qiskit import IBMQ
import qiskit
import os

IBMQX_KEY = os.environ['IBMQX_KEY']

IBMQ.save_account(IBMQX_KEY)

provider = IBMQ.load_account()

backend = provider.get_backend('ibmq_qasm_simulator')

q = qiskit.QuantumRegister(5)
c = qiskit.ClassicalRegister(5)

qc = qiskit.QuantumCircuit(q,c)

qc.measure(q,c)

job = qiskit.execute(qc, backend=backend)

print(job)


