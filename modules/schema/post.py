from common.ma import ma
from modules.post import PostModel


class PostSchema(ma.Schema):
    class Meta:
        model = PostModel