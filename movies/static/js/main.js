var ApiService = {
        _get : function(url){
        return $.ajax({
        url: url,
        });
        },
        json:undefined,
        templateURL: undefined,
        movieDetailTemplate: undefined,
        avaliableMovies: undefined,
        API_MOVIE_SEARCH: "",
        API_MOVIE_DETAIL: "",
        API_GET_WATCHLIST: "",

        getAppTemplate: function(){
            this._get(this.templateURL).done(function(response){
				this.apptemplate = response;
				});
        },
        searchMovies: function(criteria, query){
        this._get("/search_movie/?criteria="+criteria+"&query="+query).done(function(response){
        app.loadFromJson(response);
            app.render("Your favourite movies at one place");
				})
        },
        addWatchList: function(id){
        this._get("/add_in_watchlist/?movie_id="+id).done(function(response){
				})
        },
        getWatchList: function(){
            this._get("/watchlist/").done(function(response){
            app.type="wishlist"
            app.loadFromJson(response);
            app.render("your movies wishlist")
				})
        },
        getMovieDetail: function(movie_id){
            this._get("/details/?movie_id="+movie_id).done(function(response){
            swal({"title":"details","text":"Genre: " + response['genre'] + ' \nDirector: ' +response['director']});
				})
        },

}

var app = new App();

function App(){
    this.title = "";
    this.movies = [];
    this.type = "View";
    this.loadFromJson = function(json){
    if(json){
        this.movies = []
        for(var i=0; i<json.length; i++){
        var movie = new Movie()
        this.movies[i] = movie.loadFromJson(json[i]);
        }
    }
    return this;
    }
    this.searchMovies = function(){}

    this.render = function(title){
    var app = this;
    app.title = title;
    $("#title").text(app.title);
    var html = ""
    $(".table > tbody").empty();
    for(var i=0; i<this.movies.length; i++){
    if(this.type=="wishlist"){
    html += "<tr><td>"+ this.movies[i].name+"</td><td>" + this.movies[i].score+"</td><td>" + this.movies[i].popularity+"</td><td><a  id='detail_"+this.movies[i].id+"' class='btn btn-info details'>More Detail</a></td></tr>";
    }else{
    html += "<tr><td>"+ this.movies[i].name+"</td><td>" + this.movies[i].score+"</td><td>" + this.movies[i].popularity+"</td><td><a  id='"+this.movies[i].id+"' class='btn btn-default add_wishlist'>Add to watchlist</a></td><td><a  id='detail_"+this.movies[i].id+"' class='btn btn-info details'>More Detail</a></td></tr>";
    }


    }
    $(".table > tbody").append(html);
    }

}

function Movie(){
    this.id = "";
    this.name = "";
    this.score = "";
    this.popularity = "";
    this.genre = [];
    this.director = undefined;
    this.loadFromJson = function(json){
        if(json){
            this.id = json['id'];
            this.name = json['name'];
            this.score = json['score'];
            this.popularity = parseInt(json['score']) * 10;
            return this
        }
    }
    this.addToWatchList = function(){}
    this.detail = function(){}
}

$("#watchlist").on("click", function() {
	ApiService.getWatchList(app);
});

$(document).on("click", ".details", function() {
    movie_id = this.id.substring(7)
	ApiService.getMovieDetail(movie_id);
});

$(".filter").on("click", function() {
	$("#search_concept").text(this.text);
});


$("#search_movie").on("click", function() {
    var search_catagory = $("#search_concept").text();
    var search_query = $("#query")[0].value;
	ApiService.searchMovies(search_catagory, search_query);
});

$(document).on("click", ".add_wishlist", function() {
    movie_id = this.id
	ApiService.addWatchList(movie_id);
});

$(document).ready(function(){
app.loadFromJson(app_json);
app.render("Your favourite movies at one place");

});