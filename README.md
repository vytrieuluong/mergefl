# mergefl

### **Start the Director:**
./start_director.sh

### **Start Envoys:**
./start_envoy.sh
./start_envoy1.sh
./start_envoy2.sh
...
./start_envoy6.sh

### **Start the Federation and Training:**
python federated_multi_input.py

### **TensorBoard: Start TensorBoard to monitor metrics::**
tensorboard --logdir runs

### **Necessary library: PYTHON: 3.8.20:**
pip install torch torchvision numpy pandas scikit-learn pillow tqdm openfl

### **Run permission::**
chmod +x start_director.sh
chmod +x start_envoy*.sh





