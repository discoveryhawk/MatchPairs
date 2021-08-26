from models import session, User


async def get_user(telegram_id):
    return session.query(User).filter_by(telegram_id=telegram_id).first()


async def create_user(telegram_id, username, fullname):
    user = User(telegram_id=telegram_id, username=username, fullname=fullname)
    session.add(user)
    session.commit()
    return user


async def set_user_best_time(user, best_time):
    user.best_time = best_time
    session.add(user)
    session.commit()


async def get_top_10_users():
    return session.query(User).filter(User.best_time != 0).order_by(User.best_time).all()[-1:-10:-1]
