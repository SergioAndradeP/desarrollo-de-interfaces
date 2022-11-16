package com.example.myothercatalog;

import org.json.JSONArray;
import org.json.JSONException;
import org.json.JSONObject;

import java.util.ArrayList;
import java.util.List;

public class SkinsList {
    private List<Skin> skins;

    public SkinsList(JSONArray array){
        skins = new ArrayList<>();
        for(int i=0;i<array.length();i++){
            try {
                JSONObject jsonElement = array.getJSONObject(i);
                Skin skin = new Skin(jsonElement);
                skins.add(skin);
            }
            catch (JSONException ex){
                throw new RuntimeException(ex);
            }
        }
    }

    public List<Skin> getSkins() {
        return skins;
    }
}
