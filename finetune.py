import together 

if __name__ == '__main__':

    resp = together.Finetune.create(
        training_file = "file-777c8d95-621c-4af7-8bb3-d1f8175f112b",
        model = 'togethercomputer/CodeLlama-7b-Instruct',
        n_epochs = 4,
        n_checkpoints = 1,
        batch_size = 4,
        learning_rate = 1e-5,
        suffix = 'text2sql-finetune',
    )

    if 'id' in resp: 
        print(resp['id'])