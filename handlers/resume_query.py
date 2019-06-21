#!/usr/bin/env python
# coding:utf-8
import graphene
from cn import RESUME as resume_cn
from en import RESUME as resume_en

resume = {
    "cn": resume_cn,
    "en": resume_en
}


class Me(graphene.ObjectType):
    name = graphene.String()
    position = graphene.String()
    summary = graphene.String()


class Experiences(graphene.ObjectType):
    name = graphene.String()
    position = graphene.List(graphene.String)
    info = graphene.String()
    skills = graphene.List(graphene.String)
    projects = graphene.List(graphene.String)
    date = graphene.String()


class Projects(graphene.ObjectType):
    name = graphene.String()
    date = graphene.String()
    info = graphene.String()
    url = graphene.String()
    skills = graphene.List(graphene.String)
    code = graphene.List(graphene.String)


class Skills(graphene.ObjectType):
    name = graphene.String()


class ResumeQuery(graphene.ObjectType):
    me = graphene.Field(Me, language=graphene.String(required=True))
    experiences = graphene.List(Experiences, language=graphene.String(required=True))
    projects = graphene.List(Projects, language=graphene.String(required=True))
    skills = graphene.List(Skills)

    def resolve_me(self, _, language):
        data = resume.get(language, resume_cn)

        res = Me(
            name=data["name"],
            position=data["position"],
            summary=data["summary"]
        )

        return res

    def resolve_experiences(self, _, language):
        data = resume.get(language, resume_cn)
        data = data["experiences"]
        res = []

        for ex in data:
            res.append(Experiences(
                name=ex["name"],
                position=ex["position"],
                info=ex["info"],
                skills=ex["skills"],
                projects=ex["projects"],
                date=ex["date"],
            ))

        return res

    def resolve_projects(self, _, language):
        data = resume.get(language, resume_cn)
        data = data["projects"]
        res = []

        for pr in data:
            res.append(Projects(
                name=pr["name"],
                info=pr["info"],
                date=pr["date"],
                url=pr["url"],
                skills=pr["skills"],
                code=pr["code"],
            ))

        return res

    def resolve_skills(self, info):
        data = resume_en["skills"]

        res = [Skills(name=i) for i in data]

        return res


ResumeSchema = graphene.Schema(query=ResumeQuery)

if __name__ == "__main__":
    query = """
            query{
              me(language: "cn"){
                name
                position
                summary
              },
              experiences(language: "cn"){
                name
                position
                info
                skills
                projects
              },
              projects(language: "cn"){
                name
                date
                info
                url
                code
                skills
              },
              skills{
                 name
              }
            }
        """
    result = ResumeSchema.execute(query)
    print(query)
    print(result.data)
