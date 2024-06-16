#!/bin/bash

if [ "$#" -ne 3 ]; then
    echo "Usage: $0 n_epochs n_epochs_decay lr"
    exit 1
fi

# 从命令行参数获取输入
n_epochs=$1
n_epochs_decay=$2
lr=$3

# 构建 --name 参数
total=$(($n_epochs + $n_epochs_decay))
name="epoch${total}_lr${lr}"
echo "${name}"

# 运行 train.py
echo "Running training..."
python3 train.py --dataroot ./ttt --name "$name" --model pix2pix --direction AtoB --n_epochs $n_epochs --n_epochs_decay $n_epochs_decay --lr $lr

# 运行 test.py
echo "Running testing..."
python3 test.py --dataroot ./ttt --name "$name" --model pix2pix --direction Ato

echo "Scripts have completed."
