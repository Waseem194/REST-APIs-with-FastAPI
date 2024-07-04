from fastapi import APIRouter,HTTPException

from models.post import (UserPost,UserPostIn, Comment,
                            CommentIn, UserPostWithComments)


router = APIRouter()

post_table = {}
comment_table = {}

def find_post(post_id:int):
    return post_table.get(post_id)

@router.post("/post",response_model=UserPost)
async def create_comment(post:UserPostIn):
    data = post.model_dump()
    last_recode_id = len(post_table)
    new_post = {**data,"id":last_recode_id}
    post_table[last_recode_id]=new_post
    return new_post

@router.get("/post",response_model=list[UserPost])
async def get_all_post():
    return list(post_table.values())
 
@router.post("/comment",response_model=Comment)
async def create_post(comment:CommentIn):
    post = find_post(comment.post_id)
    if not post:
        raise HTTPException(status_code=404, detail={"message":"Post not found"})
    data = comment.model_dump()
    last_recode_id = len(comment_table)
    new_comment = {**data,"id":last_recode_id}
    comment_table[last_recode_id]=new_comment
    return new_comment

@router.get("/post/{post_id}/comment",response_model=list[Comment])
async def get_comments_on_post(post_id:int):
    return [
       comment for comment in comment_table.values() if comment["post_id"] == post_id
    ]
    
@router.get("/post{post_id}",response_model=UserPostWithComments)
async def get_post_with_comments(post_id:int):
    post = find_post(post_id)
    if not post:
        raise HTTPException(status_code=404, detail={"message":"Post comment not found"})
    return {
            "post":post,
            "comments": await get_comments_on_post(post_id),
        }
