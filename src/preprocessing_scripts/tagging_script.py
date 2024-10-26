import hydra
from omegaconf import DictConfig

@hydra.main(config_path="path/to/config", config_name="tags_config")
def main(cfg: DictConfig):
    tags_definitions = cfg.tags_definitions
    # Your tag assignment code here
