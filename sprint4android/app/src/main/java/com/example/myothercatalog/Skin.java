package com.example.myothercatalog;

import org.json.JSONException;
import org.json.JSONObject;

public class Skin {
    private String imageUrl;
    private String name;
    private String description;

    public Skin(JSONObject json) throws JSONException {
        this.name=json.getString("name");
        this.description=json.getString("description");
        this.imageUrl=json.getString("image_url");
    }

    public String getName() {
        return name;
    }

    public String getDescription() {
        return description;
    }

    public String getImageUrl() {
        return imageUrl;
    }

}
