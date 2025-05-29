# MessageContentPartImageURL

Represents the image URL of a message content part.

This is used to represent the image URL of a message content part in the chat completion request.
It can be either a URL or a base64 encoded image data.


## Fields

| Field                                                       | Type                                                        | Required                                                    | Description                                                 |
| ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- | ----------------------------------------------------------- |
| `detail`                                                    | *OptionalNullable[str]*                                     | :heavy_minus_sign:                                          | Specifies the detail level of the image.                    |
| `url`                                                       | *str*                                                       | :heavy_check_mark:                                          | Either a URL of the image or the base64 encoded image data. |