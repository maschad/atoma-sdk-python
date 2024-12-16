# EmbeddingObject

Individual embedding object in the response


## Fields

| Field                                            | Type                                             | Required                                         | Description                                      |
| ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ | ------------------------------------------------ |
| `embedding`                                      | List[*float*]                                    | :heavy_check_mark:                               | The embedding vector                             |
| `index`                                          | *int*                                            | :heavy_check_mark:                               | Index of the embedding in the list of embeddings |
| `object`                                         | *str*                                            | :heavy_check_mark:                               | The object type, which is always "embedding"     |