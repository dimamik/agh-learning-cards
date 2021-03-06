from flask import Flask

from app.database import regenerate_database_with_app
from app.logic.contexts.cards_collection_context import CardsCollectionContext
from app.logic.contexts.user_context import UserContext
from config import POSTGRES

app = Flask(__name__)
app.config['DEBUG'] = True

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://%(user)s:\
%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES


def init_app():
    app.app_context().push()
    regenerate_database_with_app(app)


def test():
    # usr_context = UserContext.add_new_user('username1', 'some_email@email.com', 'password')
    usr_context = UserContext.get_user_instance_by_username('username1')
    # print(usr_context.user.json())
    # cards_coll_context = CardsCollectionContext(holder_instance=usr_context.instance)
    # cards_coll_context.add_collection_to_liked(usr_context)
    cards_collection = CardsCollectionContext.get_collection_by_id(1)
    d = {'front': "Word to learn", 'back': 'Definition of the word to learn'}

    # cards_collection.add_single_card_to_collection(card_inside=d)

    # print(cards_coll_context.get_user_liked_collections(usr_context.instance.userID))
    # cards = cards_coll_context.get_all_cards_json()
    # print(cards)
    card = CardsCollectionContext.get_single_card_by_id(3)
    # CardContext(cards_coll_context.collection, single_card).add_card_to_watched(usr_context.user)
    # print(CardsCollectionContext.get_user_collections(1))
    # cardCollInstance = CardsCollectionContext(usr.user)
    # cardCollInstance = CardsCollectionContext.get_collection_by_id(6)
    # cardCollInstance.add_single_card_to_collection()
    # card = CardsCollectionContext.get_single_card_by_id(2)
    # card.change_card_inside(d)
    print(cards_collection)
    # print(cardCollInstance.cards.singleCards[0])
    # print(cardCollInstance.cards.singleCards)
    # print(cardCollInstance.cards)


if __name__ == '__main__':
    init_app()
    test()
