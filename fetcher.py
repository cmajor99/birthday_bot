GraphRequest request = GraphRequest.newMeRequest(
  accessToken,
  new GraphRequest.GraphJSONObjectCallback() {
    @Override
    public void onCompleted(JSONObject object, GraphResponse response) {
      // Insert your code here
    }
});

Bundle parameters = new Bundle();
parameters.putString("fields", "id,name,birthday");
request.setParameters(parameters);
request.executeAsync();