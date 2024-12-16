# CreateEmbeddingResponse

Response object from creating embeddings


## Fields

| Field                                                        | Type                                                         | Required                                                     | Description                                                  |
| ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `data`                                                       | List[[models.EmbeddingObject](../models/embeddingobject.md)] | :heavy_check_mark:                                           | List of embedding objects                                    |
| `model`                                                      | *str*                                                        | :heavy_check_mark:                                           | The model used for generating embeddings                     |
| `object`                                                     | *str*                                                        | :heavy_check_mark:                                           | The object type, which is always "list"                      |
| `usage`                                                      | [models.EmbeddingUsage](../models/embeddingusage.md)         | :heavy_check_mark:                                           | Usage information for the embeddings request                 |