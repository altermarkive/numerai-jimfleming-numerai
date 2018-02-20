# Numerai: Evaluator

Assuming the data is supposed to be kept in current directory the evaluator container can be run with the following command:

    docker run \
      -v $PWD:/data \
      -e STORING=/data \
      -e PUBLIC_ID="$PUBLIC_ID" \
      -e PRIVATE_SECRET="$PRIVATE_SECRET" \
      r606020/numerai-evaluator
