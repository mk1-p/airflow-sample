FRUIT=$1 # $1 은 첫번째 입력(input) 값을 의미함
if [ $FRUIT == APPLE ]; then
    echo "You selected APPLE"
elif [ $FRUIT == ORANGE ]; then
    echo "You selected ORANGE"
elif [ $FRUIT == GRAPE ]; then
    echo "You selected GRAPE"
else
    echo "You selected other $FRUIT"
fi