from flask import Flask 
from flask_restful import Api,Resource , reqparse , abort,fields,marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)
app.config["SQLALCHEMY_DATABASE_URL"] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class videoModel(db.Model) :
    id = db.Column(db.Integer,primary_key= True)
    name = db.Column(db.String(100),nullable = False)
    views = db.Column(db.Integer,nullable = False)
    likes = db.Column(db.Integer,nullable = False)

    def __repr__(self):
        return f"Video(name= {name},views ={views}, likes = {likes})"

video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type = str, help= "Name of the video is required" , required=True )
video_put_args.add_argument("views", type = int, help= "Views of the video " , required=True )
video_put_args.add_argument("likes", type = int, help= "Likes of the video" , required=True )

video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type = str, help= "Name of the video is required" )
video_update_args.add_argument("views", type = int, help= "Views of the video " )
video_update_args.add_argument("likes", type = int, help= "Likes of the video" )


resource_fields = {
    'id': fields.Integer,
    'name': fields.Integer,
    'views': fields.Integer,
    'likes': fields.Integer,
    
}
# videos = {}

# def abort_video_not_in_id (video_id):
#     if video_id not in videos :
#         abort(404, message ="Video ID is invalid")

# def abort_video_in_id (video_id) :
#     if video_id in videos :
#         abort(409,message ="video Id already exists")

class Video(Resource):
    @marshal_with(resource_fields)
    def get(self,video_id):
        result = VideoModel.query.get(id=video_id)
        # abort_video_not_in_id (video_id)
        return result 
    
    @marshal_with(resource_fields)
    def put(self,video_id):
        #abort_video_in_id(video_id)
        args = video_put_args.parse_args()
        video = videoModel(id=video_id,name=arg['name'],views=arg['views'],likes=args['likes'])
        db.session.add(video)
        db.session.commit()
        #videos[video_id] = args
        return video,201

    @marshal_with(resource_fields)
    def patch(self,video_id):
        args = video_update_args.parse_args()
        result = VideoModel.query.filter_by(id=video_id).first()
        if not result:
            abort(404, message ="Video ID is invalid,cannot update")
        if args['name']:
            result.name = args['name']
        if args['views']:
            result.views = args['views']
        if args['likes']:
            result.likes = args['likes']

        
        db.session.commit()
        return result


    def delete(self,video_id):
        abort_video_not_in_id(video_id)
        del videos[video_id]
        return " ",204
        
        #print(request.form['likes'])

api.add_resource(Video,"/video/<int:video_id>")

# names = { "arnob" : {'age':24,'gender':'male','occupation': "swe engineer"},
#           "shemin": {'age':23,'gender':'female','occupation':'architect'}
#           }
# class HelloWorld(Resource):
#     def get(self,name):
#         return names[name]
    
    # def post(self):
    #     return {'data':'Posted'}
# api.add_resource(HelloWorld,"/helloworld/<string:name>")

if __name__ == '__main__' :
    app.run(debug = True)