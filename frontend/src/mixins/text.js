var myMixin = {
    created: function (){
        this.isEmptyorWhiteSpace
    },
    methods :{
        isEmptyorWhiteSpace: function(str){
            return !str || /^\s*$/.test(str);
        }
    }
}
