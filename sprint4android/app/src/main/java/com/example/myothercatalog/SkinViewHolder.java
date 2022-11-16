package com.example.myothercatalog;

import android.view.View;
import android.widget.ImageView;
import android.widget.TextView;

import androidx.annotation.NonNull;
import androidx.recyclerview.widget.RecyclerView;

public class SkinViewHolder extends RecyclerView.ViewHolder {
    private ImageView image;
    private TextView name;
    private TextView description;

    public SkinViewHolder(@NonNull View itemView) {
        super(itemView);
        image = itemView.findViewById(R.id.skin);
        name = itemView.findViewById(R.id.title);
        description = itemView.findViewById(R.id.description);
    }

    public void ShowData(Skin skin){
        Util.downloadBitmapToImageView(skin.getImageUrl(), this.image);
        this.name.setText(skin.getName());
        this.description.setText(skin.getDescription());
    }
}
