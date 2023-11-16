from dragon_baseline import DragonBaseline


class DragonBaselineLongformerLargeEnglish4096(DragonBaseline):
    def __init__(self, **kwargs):
        """
        Adapt the DRAGON baseline to use the allenai/longformer-large-4096 model.
        Note: when manually changing the model, update the Dockerfile to pre-download that model.
        """
        super().__init__(**kwargs)
        self.model_name = "allenai/longformer-large-4096"
        self.per_device_train_batch_size = 1
        self.gradient_accumulation_steps = 8
        self.gradient_checkpointing = True
        self.max_seq_length = 4096
        self.learning_rate = 1e-05


if __name__ == "__main__":
    DragonBaselineLongformerLargeEnglish4096().process()
