import praw
r = praw.Reddit('UserStalker')
user = r.get_redditor('iamElijahWood')
limit = 1000
comment = user.get_comments(limit=limit)
for comment in comment:
  parent = r.get_info(thing_id=comment.parent_id)
	about = r.get_redditor(parent.author)
	print(parent.author,'IS ROOT?',parent.is_root,'COMMENT KARMA:',about.comment_karma,'LINK KARMA:',about.link_karma,'+18?',about.over_18,'GOLD?',about.is_gold)
