import graphene
from graphene import relay
from graphene_sqlalchemy import SQLAlchemyObjectType, SQLAlchemyConnectionField

from sqlalchemy.orm.attributes import flag_modified

from lagql_app.ext import db
from lagql_app.models import Person as PersonModel


class Person(SQLAlchemyObjectType):
    class Meta:
        model = PersonModel
        interfaces = (relay.Node, )


class Query(graphene.ObjectType):
    node = relay.Node.Field()
    all_persons = SQLAlchemyConnectionField(Person)


class CreatePerson(graphene.Mutation):
    class Arguments:
        name = graphene.String()

    ok = graphene.Boolean()
    person = graphene.Field(lambda: Person)

    def mutate(self, info, name):
        person = PersonModel(name=name)
        db.session.add(person)
        db.session.commit()
        return CreatePerson(ok=True, person=person)


class UpdatePerson(graphene.Mutation):
    class Arguments:
        id_ = graphene.Int(required=True)
        name = graphene.String(required=True)

    ok = graphene.Boolean()
    person = graphene.Field(lambda: Person)

    def mutate(self, info, id_, name):
        person = PersonModel.get_by_id(id_)

        if not id_:
            raise Exception('Must provide id_')

        if not name:
            raise Exception('Must provide name')

        if person:
           person.name = name
           person.update()
           db.session.commit()

        if not person:
            raise Exception('Person not found')

        return UpdatePerson(ok=True, person=person)


class DeletePerson(graphene.Mutation):
    class Arguments:
        id_ = graphene.Int(required=True)

    ok = graphene.Boolean()

    def mutate(self, info, **kwargs):
        person = None
        if not kwargs:
            raise Exception('Must provide id_')
        if kwargs.get('_id'):
            person = PersonModel.get(kwargs['id_'])
        else:
            person = PersonModel.get_by_id(kwargs['id_'])

        if not person:
            raise Exception('Person not found')
        person.delete()
        return DeletePerson(ok=True)


class Mutations(graphene.ObjectType):
    create_person = CreatePerson.Field()
    update_person = UpdatePerson.Field()
    delete_person = DeletePerson.Field()

schema = graphene.Schema(query=Query, mutation=Mutations)
