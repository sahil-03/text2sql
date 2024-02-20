import together 


if __name__ == '__main__':
    ft_id = 'ft-ad0569ea-aeeb-4e6a-ac79-1f9daf782397'
    print(together.Finetune.retrieve(fine_tune_id=ft_id)) # retrieves information on finetune event
    print(together.Finetune.get_job_status(fine_tune_id=ft_id)) # pending, running, completed
    print(together.Finetune.is_final_model_available(fine_tune_id=ft_id)) # True, False
    print(together.Finetune.get_checkpoints(fine_tune_id=ft_id)) # list of checkpoints
